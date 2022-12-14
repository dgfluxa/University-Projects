# frozen_string_literal: true

class CreateCourses < ActiveRecord::Migration[5.1]
  def change
    create_table :courses do |t|
      t.string :name
      t.string :sigla
      t.text :description

      t.timestamps
    end
  end
end
