// lightsUp configuration

var Configs = {};

Configs.mutation_probability = 0.5;

Configs.crossover_probability = 0.99;

Configs.generation_size = 15000;

//percent of generation to stay in the next generation
Configs.partGenerationToContinue = 0.20;

Configs.number_of_generations = 500;

//Percentage of individuals that are selected to survive the next generation - elitism
Configs.percentage_winners = 0.99;

module.exports  = Configs;