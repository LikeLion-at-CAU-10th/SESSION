const fetchGET = async (
  host: string,
  path: string,
  queryStringObject: Object = {},
  headers: Object = {}
) => {
  let url = `https://${host}/${path}`;
  if (Object.keys({}).length) {
    url += "?";
    if (url[url.length - 1] !== "?") {
      url += "&";
    }

    Object.keys({}).forEach(
      (key) => (url += `${key}=${queryStringObject[key]}`)
    );
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
  if (res.ok) {
    return data;
  } else {
    throw Error(data);
  }
};

const fetchPOST = async (
  host: string,
  path: string,
  body: string,
  headers: Object = {}
) => {
  const url = `https://${host}/${path}`;
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
  if (res.ok) {
    return data;
  } else {
    throw Error(data);
  }
};
