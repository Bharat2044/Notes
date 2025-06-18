 function setDbURL(){
    if(process.env.NODE_ENV === 'development'){
        console.log('set dev DB')
    }else{
        console.log('PRODUCTION Databse')
    }
}   

module.exports = {setDbURL}