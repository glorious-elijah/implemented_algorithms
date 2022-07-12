const linear_search = (list, target) => {
  for (let i = 0; i < list.length; i++) {
    if (target == list[i]) {
      return i;
    }
  }

  return -1;
};
