import os 


if __name__ == "__main__":
    root_dir = "."
    id = "Michael Brown"
    source = "WSJ"
    # keyword = "Michael Brown"
    keyword = "Darren Wilson;Michael Brown;Ferguson"
    # keyword = None
    root_id_path = os.path.join(os.path.join(root_dir, id))
    dir_name = os.path.join(os.path.join(root_id_path,source), keyword)

    num_pages = 36
    print(dir_name)

    # for i in range(2,num_pages+1):
    #     curr_txt_file = os.path.join(dir_name, "p"+str(i)+".txt")
    #     os.system("touch '"+curr_txt_file+"'")


    for i in range(num_pages,19,-1):
        curr_txt_file = os.path.join(dir_name, "p"+str(i-1)+".txt")
        curr_txt_file_new= os.path.join(dir_name, "p"+str(i)+".txt")
        os.system("mv '"+curr_txt_file+"' '"+curr_txt_file_new+"'")
