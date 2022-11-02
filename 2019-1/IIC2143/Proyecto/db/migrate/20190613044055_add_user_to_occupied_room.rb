# frozen_string_literal: true

class AddUserToOccupiedRoom < ActiveRecord::Migration[5.1]
  def change
    add_reference :occupied_rooms, :user, foreign_key: true
  end
end
