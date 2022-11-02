# frozen_string_literal: true

class CreatePublicacions < ActiveRecord::Migration[5.1]
  def change
    create_table :publicacions do |t|
      t.string :titulo
      t.string :user
      t.string :course
      t.text :contenido
      t.text :description
      t.integer :puntaje

      t.timestamps
    end
  end
end
