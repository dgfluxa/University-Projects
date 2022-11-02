# frozen_string_literal: true

class AddTextoToMessages < ActiveRecord::Migration[5.1]
  def change
    add_column :messages, :texto, :text
  end
end
