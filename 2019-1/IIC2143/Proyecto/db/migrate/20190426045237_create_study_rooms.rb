# frozen_string_literal: true

class CreateStudyRooms < ActiveRecord::Migration[5.1]
  def change
    create_table :study_rooms do |t|
      t.string :name
      t.string :ubication
      t.integer :availability_score
      t.integer :noise_score
      t.integer :plug_score

      t.timestamps
    end
  end
end
