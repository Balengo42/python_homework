import traceback 

try:
    with open ('diary.txt', 'a') as file:
        question1= "What happened today? "
        line = input(question1)
        file.write(line + "\n")
        while True:
           prompt = "What else? "
           line2 = input(prompt)
           file.write(line2 + "\n")
           if line2 == "done for now":
                break


except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
      print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
            
            