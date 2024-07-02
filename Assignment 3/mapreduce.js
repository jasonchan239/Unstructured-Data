function myMapper() {
    //The mapper function is called with each document, which has the special name 'this'
    //Emit a key-value pair:
    //(the mapper can emit many key-value pairs if needed)
    var hashtags = this.entities.hashtags;
    for (var i = 0; i < hashtags.length; i++) {
        var hashtag = hashtags[i];
        emit(hashtag.text, 1);
    }
}

function myReducer(key, values) {
    //The reducer is called once for each key, and is passed an array
    //containing all values corresponding to that key.
    //Produce the desired result
    return Array.sum(values);
}

db.tweets.mapReduce(myMapper, myReducer, { query: {}, out: "mroutput" })
db.mroutput.aggregate({$sort: {value: -1}})