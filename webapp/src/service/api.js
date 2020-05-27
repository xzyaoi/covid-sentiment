import axios from 'axios'

const wordcloud_endpoint = 'https://us-central1-aid-278100.cloudfunctions.net/oaf-proxy'
function fetch_wordcloud_files() {
    return new Promise((resolve, reject) => {
        axios.get(wordcloud_endpoint).then(function(res){
            resolve(res.data.data)
        }).catch(function(err){
            reject(err)
        })
    })
}


export {
    fetch_wordcloud_files,
}