import os
import shutil

# 1. اسم الفولدر اللي فيه الملفات الفوضوية (اعمله في نفس المكان)
source_folder = "my_messy_folder"

# 2. الفولدر اللي هننظم فيه الملفات
destination_folder = "organized_files"

# 3. عمل الفولدر الجديد لو مش موجود
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 4. اللف على كل ملفات الفولدر
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    # لو ده ملف فعلاً (مش فولدر)
    if os.path.isfile(file_path):
        # هنشوف امتداد الملف
        if filename.endswith(".txt"):
            target_folder = os.path.join(destination_folder, "Text_Files")
        elif filename.endswith(".jpg") or filename.endswith(".png"):
            target_folder = os.path.join(destination_folder, "Images")
        else:
            target_folder = os.path.join(destination_folder, "Others")
            
        # لو الفولدر الفرعي مش موجود نعمله
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            
        # ننقل الملف
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved: {filename}")
        
print("Done organizing!")