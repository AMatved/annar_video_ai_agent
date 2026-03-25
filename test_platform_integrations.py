"""
Test Platform Integrations for Video Creator Agent
Demonstrates account management, posting, and analytics features
"""

import sys
import os
from pathlib import Path

# Fix UTF-8 encoding on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from platform_integrations import (
    AccountManager,
    Account,
    TikTokClient,
    InstagramClient,
    YouTubeClient,
    get_client,
    PlatformAutomation,
    add_social_account,
    list_social_accounts,
    post_to_platforms,
    get_platform_analytics,
    get_registration_help,
    discover_trending_topics
)


def test_account_management():
    """Test 1: Account Management"""
    print("\n" + "="*70)
    print("🧪 TEST 1: Account Management")
    print("="*70)

    # Create account manager
    manager = AccountManager("test_accounts.json")

    # Create test accounts
    tiktok_account = Account(
        platform="tiktok",
        account_id="test_tiktok_001",
        username="fitness_creator",
        access_token="test_token_123",
        display_name="Fitness Creator Channel"
    )

    instagram_account = Account(
        platform="instagram",
        account_id="test_insta_001",
        username="lifestyle_daily",
        access_token="test_token_456",
        display_name="Lifestyle Daily"
    )

    youtube_account = Account(
        platform="youtube",
        account_id="test_youtube_001",
        username="tech_reviewer",
        access_token="test_token_789",
        display_name="Tech Reviewer"
    )

    # Add accounts
    print("\n📝 Adding accounts...")
    print(manager.add_account(tiktok_account))
    print(manager.add_account(instagram_account))
    print(manager.add_account(youtube_account))

    # List all accounts
    print("\n" + manager.list_accounts())

    # Get specific account
    print("\n🔍 Getting specific TikTok account...")
    account = manager.get_account("tiktok", "fitness_creator")
    if account:
        print(f"✅ Found: {account.username} ({account.display_name})")

    # Remove account
    print("\n🗑️  Removing Instagram account...")
    print(manager.remove_account("instagram", "lifestyle_daily"))

    print("\n📋 Updated account list:")
    print(manager.list_accounts())

    return True


def test_api_clients():
    """Test 2: API Clients (Mock Responses)"""
    print("\n" + "="*70)
    print("🧪 TEST 2: API Clients")
    print("="*70)

    # Create test account
    account = Account(
        platform="tiktok",
        account_id="test_001",
        username="test_user",
        access_token="test_token"
    )

    # Test TikTok client
    print("\n🎵 Testing TikTok Client...")
    tiktok_client = TikTokClient(account)

    # Post video (mock)
    result = tiktok_client.post_video(
        video_path="test_video.mp4",
        caption="Test video #fyp #viral",
        hashtags=["#fyp", "#viral"]
    )
    print(f"📤 Post result: {result.get('message', result.get('error'))}")

    # Get analytics (mock)
    analytics = tiktok_client.get_analytics()
    if analytics.get("success"):
        print(f"📊 Analytics:")
        print(f"   Views: {analytics.get('views')}")
        print(f"   Likes: {analytics.get('likes')}")
        print(f"   Engagement: {analytics.get('engagement_rate')}")

    # Test trending hashtags
    print("\n🔥 Testing trending hashtags discovery...")
    hashtags = tiktok_client.discover_trending_hashtags("fitness")
    print(f"Trending fitness hashtags: {', '.join(hashtags[:5])}")

    return True


def test_platform_automation():
    """Test 3: Platform Automation"""
    print("\n" + "="*70)
    print("🧪 TEST 3: Platform Automation")
    print("="*70)

    automation = PlatformAutomation("test_accounts.json")

    # Get analytics for all accounts
    print("\n📊 Getting analytics for all accounts...")
    analytics = automation.get_all_analytics()

    for account_key, data in analytics.items():
        if data.get("success"):
            print(f"\n✅ {account_key}:")
            print(f"   Views: {data.get('views')}")
            print(f"   Likes: {data.get('likes')}")
            print(f"   Engagement: {data.get('engagement_rate')}")
        else:
            print(f"\n❌ {account_key}: {data.get('error')}")

    # Discover trends
    print("\n🔥 Discovering trending topics...")
    trends = automation.discover_trends("fitness", "tiktok")
    if trends:
        print(f"Trending hashtags for fitness: {', '.join(trends[:7])}")

    return True


def test_agent_integration():
    """Test 4: Agent Integration Functions"""
    print("\n" + "="*70)
    print("🧪 TEST 4: Agent Integration Functions")
    print("="*70)

    # Test list_social_accounts
    print("\n📋 Testing list_social_accounts()...")
    result = list_social_accounts()
    print(result)

    # Test get_platform_analytics
    print("\n📊 Testing get_platform_analytics()...")
    analytics = get_platform_analytics("tiktok", "fitness_creator")
    print(analytics)

    # Test get_registration_help
    print("\n📖 Testing get_registration_help()...")
    help_text = get_registration_help("tiktok")
    print(help_text[:500] + "...")  # Print first 500 chars

    # Test discover_trending_topics
    print("\n🔥 Testing discover_trending_topics()...")
    trends = discover_trending_topics("fitness", "tiktok")
    print(trends)

    return True


def test_multi_account_scenario():
    """Test 5: Multi-Account Scenario"""
    print("\n" + "="*70)
    print("🧪 TEST 5: Multi-Account Scenario (Content Creator Agency)")
    print("="*70)

    manager = AccountManager("test_accounts.json")

    # Simulate agency with multiple accounts
    agency_accounts = [
        Account("tiktok", "client1_tt", "client1_fitness", display_name="Client 1 - Fitness"),
        Account("tiktok", "client2_tt", "client2_cooking", display_name="Client 2 - Cooking"),
        Account("instagram", "client1_ig", "client1_lifestyle", display_name="Client 1 - Lifestyle"),
        Account("instagram", "client2_ig", "client2_travel", display_name="Client 2 - Travel"),
        Account("youtube", "client1_yt", "client1_tech", display_name="Client 1 - Tech"),
    ]

    print("\n📝 Adding agency client accounts...")
    for acc in agency_accounts:
        manager.add_account(acc)

    print("\n📊 Agency accounts overview:")
    print(manager.list_accounts())

    # Get analytics for all client accounts
    automation = PlatformAutomation("test_accounts.json")
    print("\n📈 Client performance summary:")
    analytics = automation.get_all_analytics()

    for account, data in analytics.items():
        if data.get("success"):
            print(f"  {account}: {data['views']} views, {data['engagement_rate']} engagement")

    print("\n✅ Multi-account scenario test complete!")
    return True


def cleanup_test_files():
    """Clean up test files"""
    print("\n" + "="*70)
    print("🧹 Cleaning up test files...")
    print("="*70)

    test_files = [
        "test_accounts.json",
        "accounts.json"
    ]

    for file in test_files:
        if Path(file).exists():
            Path(file).unlink()
            print(f"  🗑️  Removed {file}")
        else:
            print(f"  ℹ️  {file} not found")

    print("\n✅ Cleanup complete!")


def main():
    """Run all tests"""
    print("\n" + "="*70)
    print("🎬 PLATFORM INTEGRATIONS TEST SUITE")
    print("Video Creator Agent v3.0")
    print("="*70)

    tests = [
        ("Account Management", test_account_management),
        ("API Clients", test_api_clients),
        ("Platform Automation", test_platform_automation),
        ("Agent Integration", test_agent_integration),
        ("Multi-Account Scenario", test_multi_account_scenario),
    ]

    passed = 0
    failed = 0

    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"\n✅ {test_name} - PASSED")
        except Exception as e:
            failed += 1
            print(f"\n❌ {test_name} - FAILED: {str(e)}")

    # Summary
    print("\n" + "="*70)
    print("📊 TEST SUMMARY")
    print("="*70)
    print(f"✅ Passed: {passed}/{len(tests)}")
    print(f"❌ Failed: {failed}/{len(tests)}")

    if failed == 0:
        print("\n🎉 All tests passed successfully!")

    # Cleanup
    print("\n")
    cleanup_test_files()

    print("\n" + "="*70)
    print("🎯 Test suite complete!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
