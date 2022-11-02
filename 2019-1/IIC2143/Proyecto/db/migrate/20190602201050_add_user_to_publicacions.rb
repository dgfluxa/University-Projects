# frozen_string_literal: true

class AddUserToPublicacions < ActiveRecord::Migration[5.1]
  def change
    remove_column :publicacions, :user, :string
    add_reference :publicacions, :user, foreign_key: true
  end
end
