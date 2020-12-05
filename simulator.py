def loop_simulation(LOOPS = 11,thread = 0):
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
                            if (loop_count > LOOPS):
                                return
                            print("va = [ a[",ii,"][",kk,"] , a[",ii,"][",kk,"] , a[",ii,"][",kk,"] ,  a[",ii,"][",kk,"] ]")
                            print("vb = [ b[",kk,"][",jj,"] , b[",kk,"][",jj+1,"] , b[",kk,"][",jj+2,"] , b[",kk,"][",jj+3,"] ]")
                               
                            print("Multiplication Step")
                            print("  c[",ii,"][",jj,"] = c[",ii,"][",jj,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj,"])" )
                            print("  c[",ii,"][",jj+1,"] = c[",ii,"][",jj+1,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+1,"])" )
                            print("  c[",ii,"][",jj+2,"] = c[",ii,"][",jj+2,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+2,"])" )
                            print("  c[",ii,"][",jj+3,"] = c[",ii,"][",jj+3,"] + (a[",ii,"][",kk,"] * b[",kk,"][",jj+3,"])" )
                            print("==================================================================")
                            loop_count = loop_count + 1
                               

    return

if __name__ == "__main__":
    loops = int(input("Enter Number of Loops: "))
    thread = int(input("Enter which thread you want to simulate: "))
    loop_simulation(LOOPS = loops, thread = thread)
