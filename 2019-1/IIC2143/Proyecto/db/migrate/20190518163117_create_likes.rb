# frozen_string_literal: true

class CreateLikes < ActiveRecord::Migration[5.1]
  def change
    create_table :likes do |t|
      t.references :user, foreign_key: true
      t.references :publicacion, foreign_key: true
      t.integer :like

      t.timestamps
    end
  end
end
