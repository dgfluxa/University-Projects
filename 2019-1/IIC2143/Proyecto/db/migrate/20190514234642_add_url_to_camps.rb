# frozen_string_literal: true

class AddUrlToCamps < ActiveRecord::Migration[5.1]
  def change
    add_column :camps, :url, :string
  end
end
