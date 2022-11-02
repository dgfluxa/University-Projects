# frozen_string_literal: true

class CreatePublicacionComments < ActiveRecord::Migration[5.1]
  def change
    create_table :publicacion_comments do |t|
      t.text :body
      t.references :user, foreign_key: true
      t.references :publicacion, foreign_key: true

      t.timestamps
    end
  end
end
