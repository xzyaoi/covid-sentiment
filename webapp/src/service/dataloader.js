import Papa from 'papaparse'

function load_data(objectId) {
    const url = 'https://files.de-1.osf.io/v1/resources/vej5u/providers/osfstorage/'+objectId
    return new Promise((resolve, reject)=>{
        Papa.parse(url, {
            download: true,
            error: function (err, file, inputElem, reason) {
                const message = 'error csv downloader & parser: ' + reason;
                console.error(message);
                reject(message);
            },
            complete: function(results) {
                resolve(results)
            },
        })
    })
}

export {
    load_data
}