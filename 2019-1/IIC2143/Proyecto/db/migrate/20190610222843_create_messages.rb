# frozen_string_literal: true

class CreateMessages < ActiveRecord::Migration[5.1]
  def change
    create_table :messages do |t|
      t.references :user1
      t.references :user2
      t.references :conversation, foreign_key: true

      t.timestamps
    end
  end
end
