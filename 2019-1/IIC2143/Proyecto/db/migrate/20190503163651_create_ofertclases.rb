# frozen_string_literal: true

class CreateOfertclases < ActiveRecord::Migration[5.1]
  def change
    create_table :ofertclases do |t|
      t.integer :precio
      t.string :course
      t.string :sala
      t.text :description
      t.integer :time

      t.timestamps
    end
  end
end
