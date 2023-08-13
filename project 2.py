import os
import sys
def find_largest_file(path, num_file =10):
  file_info = []
  for root,dirs,files in os.walk(path):
      for filename in files:
          file_path = os.path.join(root,filename)
          file_size = os.path.getsize(file_path)
          file_info.append((file_path,file_size))
  sorted_files = sorted(file_info, key = lambda x:x[1], reverse = True)
  print(f"Top files{num_file} largest file in  '{path}'")
  for i,(file_path, file_size) in enumerate(sorted_files[:num_file],start =1):
      print(f"{i}.File:{file_path}\n SIze: {file_size} bytes\n")

  if __name__ == "__main__":
      if len(sys.argv) < 2:
          print("Usage: python largest_files_finder.py <path> [num_files]")
          sys.exit(1)

      if len(sys.argv)>2:
          num_file = int(sys.argv[2])
      find_largest_file(path, num_file)