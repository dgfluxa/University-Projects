# frozen_string_literal: true

class CreateSubscribedUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :subscribed_users do |t|
      t.references :study_group, foreign_key: true
      t.references :user, foreign_key: true

      t.timestamps
    end
  end
end
