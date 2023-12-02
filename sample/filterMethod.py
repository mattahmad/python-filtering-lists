def filter_height(height):
    if (height < 150):
        return True
    else:
        return False
  
heights = [140, 180, 165, 162, 145]
filtered_heights = filter(filter_height, heights)


print(list(filtered_heights))