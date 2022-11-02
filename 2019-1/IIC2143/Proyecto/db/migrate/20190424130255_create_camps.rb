# frozen_string_literal: true

class CreateCamps < ActiveRecord::Migration[5.1]
  def change
    create_table :camps do |t|
      t.string :nombre
      t.string :ubicacion
      t.string :lat
      t.string :long

      t.timestamps
    end
  end
end
