export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      const newObj = {
        status: 200,
        body: 'Success',
      };
      resolve(newObj);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
