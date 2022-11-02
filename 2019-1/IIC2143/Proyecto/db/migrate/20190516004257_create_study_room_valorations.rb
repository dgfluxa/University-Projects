# frozen_string_literal: true

class CreateStudyRoomValorations < ActiveRecord::Migration[5.1]
  def change
    create_table :study_room_valorations do |t|
      t.integer :availability
      t.integer :noise
      t.integer :plugs
      t.references :user, foreign_key: true
      t.references :study_room, foreign_key: true

      t.timestamps
    end
  end
end
