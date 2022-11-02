# frozen_string_literal: true

class CreateStudyRoomComments < ActiveRecord::Migration[5.1]
  def change
    create_table :study_room_comments do |t|
      t.references :user, foreign_key: true
      t.text :body
      t.references :study_room, foreign_key: true

      t.timestamps
    end
  end
end
