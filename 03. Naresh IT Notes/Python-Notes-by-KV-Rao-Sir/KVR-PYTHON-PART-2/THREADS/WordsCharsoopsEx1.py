#Program for accepting Line of text and  display words and Chars by using threads
#WordsCharsoopsEx1.py
import threading,time
class WordsChars:
	def generate(self,line):
		if(len(line)==0):
			print("{}--->Line of Text is Empty:".format(threading.current_thread().name))
		else:
			print("-------------------------------------------------")
			print("{}--->Given Line of Text:{}".format(threading.current_thread().name,line))
			print("-------------------------------------------------")
			words=line.split()
			for word in words:#For Word Display
				print(word)
				time.sleep(0.5)
				for ch in word: # For Chars of Word
					print("\t{}".format(ch))
					time.sleep(0.30)
			print("-------------------------------------------------")

#main Program
line=input("Enter Line of Text:")
t1=threading.Thread(target=WordsChars().generate,args=(line,))
t1.start()
