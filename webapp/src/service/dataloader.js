import Papa from 'papaparse'

function load_data(objectId) {
    console.log(objectId)
    objectId = '5-24'
    const url = 'https://raw.githubusercontent.com/xzyaoi/covid-sentiment/master/data/'+objectId+'.csv'
    return new Promise((resolve, reject)=>{
        Papa.parse(url, {
            download: true,
            error: function (err, file, inputElem, reason) {
                const message = 'error csv downloader & parser: ' + reason;
                console.log(message);
                reject(message);
            },
            complete: function(results) {
                let data = results.data
                resolve(data.slice(1, data.length))
            },
        })
    })
}

export {
    load_data
}