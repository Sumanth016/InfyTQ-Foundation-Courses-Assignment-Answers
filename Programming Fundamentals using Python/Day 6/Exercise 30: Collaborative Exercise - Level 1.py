#PF-Exer-30

def find_average(mark_list):
	total=0
	try:
	    for i in range(0, len(mark_list)):
		    total+=mark_list[i]
	    marks_avg= total/len(mark_list)
	    return marks_avg
	except:
	    print("Some error Occurred")
      
try:
    mark_list=[1,2,3,4]
    print("Average marks:", find_average(mark_list))
except TypeError:
    print("Type error")
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Zero Division Error Occurred")
except NameError:
    print("Invocation name error")
except:
    print("Some error Occurred")
finally:
    print("Finally")
    
'''
Average marks: 2.5
Finally
'''
