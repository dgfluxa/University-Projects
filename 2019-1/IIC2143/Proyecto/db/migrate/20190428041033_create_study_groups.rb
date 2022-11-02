# frozen_string_literal: true

class CreateStudyGroups < ActiveRecord::Migration[5.1]
  def change
    create_table :study_groups do |t|
      t.references :course, foreign_key: true
      t.references :study_room, foreign_key: true
      t.integer :max
      t.integer :duration

      t.timestamps
    end
  end
end
