# frozen_string_literal: true

class AddCampIdToStudyRooms < ActiveRecord::Migration[5.1]
  def change
    add_column :study_rooms, :camp_id, :integer
  end
end
