def loop_simulation(thread = 0):
    ARRAY_SIZE = 4096
    n = 512
    tid = thread
    number_of_threads = 4
    loop_count = 0
    VECTOR_WIDTH = 4
    for i in range(int((ARRAY_SIZE/number_of_threads)*tid),int((ARRAY_SIZE)/number_of_threads*(tid+1)), int(ARRAY_SIZE/n)):
        for j in range(0,ARRAY_SIZE,int(ARRAY_SIZE/n)):
            for k in range(0,ARRAY_SIZE,int(ARRAY_SIZE/n)):
                for ii in range(i,int(i+(ARRAY_SIZE/n))):
                    for jj in range(j,int(j+(ARRAY_SIZE/n)),VECTOR_WIDTH):
                        for kk in range(k,int(k+(ARRAY_SIZE/n))):
                            print("va = [ a[",ii,"][",kk,"] , a[",ii,"][",kk,"] , a[",ii,"][",kk,"] ,  a[",ii,"][",kk,"] ]")
                            print("vb = [ b[",kk,"][",jj,"] , b[",kk,"][",jj+1,"] , b[",kk,"][",jj+2,"] , b[",kk,"][",jj+3,"] ]")
                               
                            print("Multiplication Step")
                            print("  c[",ii,"][",jj,"] = c[",ii,"][",jj,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj,"])" )
                            print("  c[",ii,"][",jj+1,"] = c[",ii,"][",jj+1,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+1,"])" )
                            print("  c[",ii,"][",jj+2,"] = c[",ii,"][",jj+2,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+2,"])" )
                            print("  c[",ii,"][",jj+3,"] = c[",ii,"][",jj+3,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+3,"])" )
                            print("==================================================================")
    return

def loop_step_simulation(LOOPS = 11,thread = 0):
    ARRAY_SIZE = 4096
    n = 512
    tid = thread
    number_of_threads = 4
    loop_count = 0
    VECTOR_WIDTH = 4
    m_step = -1
    for i in range(int((ARRAY_SIZE/number_of_threads)*tid),int((ARRAY_SIZE)/number_of_threads*(tid+1)), int(ARRAY_SIZE/n)):
        for j in range(0,ARRAY_SIZE,int(ARRAY_SIZE/n)):
            for k in range(0,ARRAY_SIZE,int(ARRAY_SIZE/n)):
                for ii in range(i,int(i+(ARRAY_SIZE/n))):
                    for jj in range(j,int(j+(ARRAY_SIZE/n)),VECTOR_WIDTH):
                        for kk in range(k,int(k+(ARRAY_SIZE/n))):
                            if (loop_count > LOOPS):
                                return
                            print("va = [ a[",ii,"][",kk,"] , a[",ii,"][",kk,"] , a[",ii,"][",kk,"] ,  a[",ii,"][",kk,"] ]")
                            print("vb = [ b[",kk,"][",jj,"] , b[",kk,"][",jj+1,"] , b[",kk,"][",jj+2,"] , b[",kk,"][",jj+3,"] ]")
                            m_step = m_step + 1  
                            print("Multiplication Step ", m_step)
                            print("  c[",ii,"][",jj,"] = c[",ii,"][",jj,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj,"])" )
                            print("  c[",ii,"][",jj+1,"] = c[",ii,"][",jj+1,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+1,"])" )
                            print("  c[",ii,"][",jj+2,"] = c[",ii,"][",jj+2,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+2,"])" )
                            print("  c[",ii,"][",jj+3,"] = c[",ii,"][",jj+3,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+3,"])" )
                            print("==================================================================")
                            loop_count = loop_count + 1
    return

def count_accesses(thread):
    ARRAY_SIZE = 4096
    n = 512
    tid = thread
    number_of_threads = 4
    loop_count = 0
    VECTOR_WIDTH = 4
    access_count = 0
    for i in range(int((ARRAY_SIZE/number_of_threads)*tid),int((ARRAY_SIZE)/number_of_threads*(tid+1)), int(ARRAY_SIZE/n)):
        for j in range(0,ARRAY_SIZE,int(ARRAY_SIZE/n)):
            for k in range(0,ARRAY_SIZE,int(ARRAY_SIZE/n)):
                for ii in range(i,int(i+(ARRAY_SIZE/n))):
                    for jj in range(j,int(j+(ARRAY_SIZE/n)),VECTOR_WIDTH):
                        for kk in range(k,int(k+(ARRAY_SIZE/n))):
                          if(kk == 0 and jj == 0):
                            access_count = access_count + 1
    print("Number of accesses of b[0][0]  is ", access_count);                        
    return

if __name__ == "__main__":
	print("1. Loop Step Simulation")
	print("2. Regular Simulation")
	print("3. Count number of accesses")
	menu_choice = int(input("Enter Menu Choice:"))
	if( menu_choice is 1):
		loops = int(input("Enter Number of Loops: "))
		thread = int(input("Enter which thread you want to simulate: "))
		loop_step_simulation(LOOPS = loops, thread = thread)
	elif( menu_choice is 2):
		thread = int(input("Enter which thread you want to simulate: "))
		loop_simulation(thread)
	elif( menu_choice is 3):
		thread = int(input("Enter which thread you want to simulate: "))
		count_accesses(thread)
	else:
		pass
