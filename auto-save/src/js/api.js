export default (text) => {
  let delayed = null;
  return new Promise((resolve) => {
    delayed = setInterval(() => {
      return resolve(text);
    }, 1000);
  }).finally((resolved) => {
    console.log(resolved);
    clearInterval(delayed);
  });
};
