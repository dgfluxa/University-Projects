# frozen_string_literal: true

class RemoveColumnsFromCamps < ActiveRecord::Migration[5.1]
  def change
    remove_column :camps, :lat, :string
    remove_column :camps, :long, :string
  end
end
