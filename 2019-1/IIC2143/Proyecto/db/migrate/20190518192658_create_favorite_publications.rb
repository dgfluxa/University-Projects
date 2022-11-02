# frozen_string_literal: true

class CreateFavoritePublications < ActiveRecord::Migration[5.1]
  def change
    create_table :favorite_publications do |t|
      t.references :publicacion, foreign_key: true
      t.references :user, foreign_key: true

      t.timestamps
    end
  end
end
