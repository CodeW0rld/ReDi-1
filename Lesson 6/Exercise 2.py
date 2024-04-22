story = "story.txt"
with open (story, "r") as file:
    file.write("As she sat in front of her computer, fingers furiously tapping away at the keyboard, Sarah felt like she was casting a spell. Lines of code appeared on the screen, twisting and turning like a serpent. She was a master of Python, the programming language that had captured her heart. With each line she wrote, Sarah's imagination came to life. She created worlds and characters with just a few commands. Her code was a canvas, and she was the artist. As the clock struck midnight, Sarah's masterpiece was complete. She sat back, admiring her creation, a story told through lines of Python code. It was a magical feeling, and she couldn't wait to share it with the world.")
with open(file, "r") as file:
    lines = file.readlines()

res = {}

for line in lines:
    key, value = line.strip().split(':')
    res[key.strip()] = value.strip()
     
print("Dictionary Created:")
print(res)