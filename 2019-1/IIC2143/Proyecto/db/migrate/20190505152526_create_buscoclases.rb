# frozen_string_literal: true

class CreateBuscoclases < ActiveRecord::Migration[5.1]
  def change
    create_table :buscoclases do |t|
      t.string :user
      t.string :course
      t.integer :time
      t.integer :id_grupo

      t.timestamps
    end
  end
end
