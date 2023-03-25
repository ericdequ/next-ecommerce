exports.seed = function (knex) {
  // Deletes ALL existing entries
  return knex('category')
    .del()
    .then(function () {
      // Inserts seed entries
      return knex('category').insert([
        {
          id: 1,
          name: 'mushroom',
          label: 'Mushroom',
          md_icon: 'MdSpa',
          created_at: Date.now(),
        },
        {
          id: 2,
          name: 'delta-8',
          label: 'Delta-8',
          md_icon: 'MdSmokeFree',
          created_at: Date.now(),
        },
        {
          id: 3,
          name: 'cbd',
          label: 'CBD',
          md_icon: 'MdLocalPharmacy',
          created_at: Date.now(),
        },
        {
          id: 4,
          name: 'delta-9',
          label: 'Delta-9',
          md_icon: 'MdSmokeFree',
          created_at: Date.now(),
        },
        {
          id: 5,
          name: 'supplements',
          label: 'Supplements',
          md_icon: 'MdLocalPharmacy',
          created_at: Date.now(),
        },
      ]);
    });
};
