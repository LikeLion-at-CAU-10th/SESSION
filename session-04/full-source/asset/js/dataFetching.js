const fetchGET = async (host, path, queryStringObject = {}, headers = {}) => {
  let url = `${host}${path}`;
  if (Object.keys(queryStringObject).length) {
    url += "?";

    Object.keys(queryStringObject).forEach((key) => {
      if (url[url.length - 1] !== "?") {
        url += "&";
      }
      url += `${key}=${queryStringObject[key]}`;
    });
  }

  const options = {
    method: "GET",
    header: {
      "Content-Type": "application/json",
      ...headers,
    },
  };

  const res = await fetch(url, options);
  const data = await res.json();

  return data;
};

const fetchPOST = async (host, path, body, headers = {}) => {
  const url = `${host}${path}`;
  const options = {
    method: "POST",
    header: {
      "Content-Type": "application/json",
      ...headers,
    },
    body: JSON.stringify(body),
  };

  const res = await fetch(url, options);
  const data = await res.json();

  return data;
};

export { fetchGET, fetchPOST };
