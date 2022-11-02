# frozen_string_literal: true

class CreateOccupiedRooms < ActiveRecord::Migration[5.1]
  def change
    create_table :occupied_rooms do |t|
      t.references :study_room, foreign_key: true
      t.datetime :from
      t.datetime :to

      t.timestamps
    end
  end
end
