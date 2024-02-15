#!/usr/bin/node
const axios = require('axios');

async function getMovieCharacters(movieId) {
  try {
    const filmResponse = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    const charactersUrls = filmResponse.data.characters;

    for (const characterUrl of charactersUrls) {
      const characterResponse = await axios.get(characterUrl);
      const characterName = characterResponse.data.name;
      console.log(characterName);
    }
  } catch (error) {
    console.error(`Error fetching data: ${error.message}`);
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);

