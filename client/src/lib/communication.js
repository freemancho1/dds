const apiHeader = {"Content-Type": "application/json"};

const apiUrls = {
    samples: "http://localhost:11000/samples",
    predict: "http://localhost:11000/predict",
    rePredict: "http://localhost:11000/re_predict",
}

export async function reqGET(urlCode) {
    const response = await fetch(apiUrls[urlCode], {
        method: "GET", headers: apiHeader
    });
    const data = response.json();

    if (response.ok) {
        return data;
    } else {
        throw new Error(data);
    }
}

export async function reqPOST(urlCode, promise) {
    const postData = await promise;
    const response = await fetch(apiUrls[urlCode], {
        method: "POST", headers: apiHeader,
        body: JSON.stringify(postData),
    });
    const data = response.json()

    if (response.ok) {
        return data;
    } else {
        throw new Error(data);
    }
}