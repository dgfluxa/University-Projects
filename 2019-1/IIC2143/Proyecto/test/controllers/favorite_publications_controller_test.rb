# frozen_string_literal: true

require 'test_helper'

class FavoritePublicationsControllerTest < ActionDispatch::IntegrationTest
  test 'should get update' do
    get favorite_publications_update_url
    assert_response :success
  end
end
