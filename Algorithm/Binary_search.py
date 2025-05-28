def binary_search(arr, target, start_idx, end_idx):
    if start_idx > end_idx: return False
    
    mid_idx = (start_idx+end_idx)//2 
    if arr[mid_idx] == target: return mid_idx
    elif arr[mid_idx] > target:
        return binary_search(arr, target, start_idx, mid_idx-1)
    else:
        return binary_search(arr, target, start_idx+1, end_idx)