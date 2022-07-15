# tower of hanoi program
def tower_of_hanoi(source,destination,auxillary,no_of_disk):
    if no_of_disk==1:
        print("Move disk 1 from",source,"to",destination)
        return
    tower_of_hanoi(source,auxillary,destination,no_of_disk-1)
    print("Move disk",no_of_disk,"from source",source,"to destination",destination)
    tower_of_hanoi(auxillary,destination,source,no_of_disk-1)

if __name__=="__main__":
    no_of_disk=int(input("Enter no of disk:"))
    tower_of_hanoi('A','C','B',no_of_disk)
