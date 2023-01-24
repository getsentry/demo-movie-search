class CreateShows < ActiveRecord::Migration[7.0]
  def change
    create_table :shows do |t|
      t.string :show_type
      t.string :title
      t.string :countries
      t.date :date_added
      t.integer :release_year
      t.string :rating
      t.string :duration
      t.string :categories
      t.text :description

      t.timestamps
    end
  end
end
