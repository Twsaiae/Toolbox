from cleanvision.imagelab import Imagelab

if __name__ == "__main__":
    path = r"E:\下载\image_files\image_files"
    imagelab = Imagelab(data_path=path)  # initialize imagelab

    imagelab.find_issues()  # Find issues in the dataset
    print(imagelab.issue_summary)

    for issues in list(imagelab.issue_summary["issue_type"]):
        bad_image_list = imagelab.issues[imagelab.issues[f"is_{issues}_issue"] == True].index.to_list()
        print(f"{issues}这个类型错误的图片有{len(bad_image_list)}，分别是{bad_image_list}")
        imagelab.visualize(image_files=imagelab.issues[imagelab.issues[f"is_{issues}_issue"] == True].index.to_list())
