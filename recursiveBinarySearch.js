const recursiveBinarySearch = (list, target) => {
  let first = 0;
  let last = list.length - 1;

  if (list.length === 0) {
    return false;
  } else {
    let mid = Math.floor((first + last) / 2);
    if (target === list[mid]) {
      return true;
    } else if (target > list[mid]) {
      let new_list = list.slice(mid + 1);
      return recursiveBinarySearch(new_list, target);
    } else {
      let new_list = list.slice(0, mid - 1);
      return recursiveBinarySearch(new_list, target);
    }
  }
};
