let chai = require('chai')
let chaiHttp = require('chai-http');
chai.use(chaiHttp);
const expect = chai.expect;

describe('Testing ToDo Application', () => {
    it('It should return 404 for /abc', (done) => {
        chai.request('http://localhost:5000').get('/abc').then(res => {
            expect(res).to.have.status(404);
            done();
        })
    })
    it('should return status 200 for / route', (done) => {
        chai.request('http://localhost:5000').get('/').then(res => {
            expect(res).to.have.status(200);
            done();
        })
    });
    it('should return status 200 for /api/todos route', (done) => {
        chai.request('http://localhost:5000').get('/api/todos').then(res => {
            expect(res).to.have.status(200);
            expect(res.body).to.be.an('array');
            expect(res.body).to.have.length(4);
            done();
        })
    });
});