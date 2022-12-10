import os

if __name__ == "__main__":
    base_path = os.getcwd()
    imagefile_names = os.listdir(base_path + "/test_clothes")    
    peoplefile_names = os.listdir(base_path + "/test_img")

    demo_contents = []
    for peoplefile_name in peoplefile_names:
        for imagefile_name in imagefile_names:
            demo_contents.append(peoplefile_name + " " + imagefile_name)
    
    # print(demo_contents)
    with open("demo.txt", "w") as f:
        for content in demo_contents:
            f.write(content + "\n")