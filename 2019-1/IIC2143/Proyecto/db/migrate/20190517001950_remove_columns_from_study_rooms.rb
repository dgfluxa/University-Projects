# frozen_string_literal: true

class RemoveColumnsFromStudyRooms < ActiveRecord::Migration[5.1]
  def change
    remove_column :study_rooms, :availability_score, :integer
    remove_column :study_rooms, :noise_score, :integer
    remove_column :study_rooms, :plug_score, :integer
  end
end
